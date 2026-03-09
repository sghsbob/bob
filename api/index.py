import os, re, httpx, asyncio
from datetime import datetime, timedelta, timezone
from flask import Flask, request, jsonify

app = Flask(__name__)
KST = timezone(timedelta(hours=9))
NEIS_KEY = os.getenv("NEIS_API_KEY", "")
OFFICE_CODE = os.getenv("OFFICE_CODE", "")
SCHOOL_CODE = os.getenv("SCHOOL_CODE", "")
TG_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

async def fetch_meal(date_str):
    url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {'KEY': NEIS_KEY, 'Type': 'json', 'ATPT_OFCDC_SC_CODE': OFFICE_CODE, 'SD_SCHUL_CODE': SCHOOL_CODE, 'MLSV_YMD': date_str}
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get(url, params=params, timeout=5)
            data = res.json()
            if 'mealServiceDietInfo' not in data: return None
            meals = {row['MMEAL_SC_NM']: re.sub(r'\([0-9.]+\)', '', row['DDISH_NM'].replace('<br/>', '\n')).strip() for row in data['mealServiceDietInfo'][1]['row']}
            return meals
    except: return None

def parse_date(text):
    now = datetime.now(KST)
    text = text.replace(" ", "")
    if "내일" in text: now += timedelta(1)
    elif "모레" in text: now += timedelta(2)
    elif "어제" in text: now -= timedelta(1)
    m = re.search(r'(\d{4})[-/]?(\d{2})[-/]?(\d{2})', text)
    return f"{m.group(1)}{m.group(2)}{m.group(3)}" if m else now.strftime('%Y%m%d')

def res_kakao(text):
    qr = [{"label": l, "action": "message", "messageText": l} for l in ["오늘의급식", "내일의급식"]]
    return jsonify({"version": "2.0", "template": {"outputs": [{"simpleText": {"text": text.strip()}}], "quickReplies": qr}})

@app.route('/')
def home(): return "SGHS Bob Bot"

@app.route('/api/kakao', methods=['GET', 'POST'])
async def kakao():
    ut = (request.get_json(silent=True) or {}).get("userRequest", {}).get("utterance", "")
    if any(k in ut for k in ["도움", "알림", "주간", "이번주"]): return res_kakao("준비중입니다!")
    d = parse_date(ut)
    m = await fetch_meal(d)
    if not m: return res_kakao(f"[{d}] 급식 정보가 없습니다.")
    return res_kakao(f"🍱 {d} 급식\n" + "\n".join([f"\n{k}\n{v}" for k, v in m.items()]))

@app.route('/api/telegram', methods=['POST'])
async def telegram():
    upd = request.get_json(silent=True) or {}
    if "message" not in upd or not TG_TOKEN: return "ok"
    cid, ut = upd["message"]["chat"]["id"], upd["message"].get("text", "")
    d, m = parse_date(ut), await fetch_meal(parse_date(ut))
    rep = f"🍱 <b>{d} 급식</b>\n" + "\n".join([f"\n<b>[{k}]</b>\n{v}" for k, v in m.items()]) if m else f"[{d}] 급식 정보가 없습니다."
    async with httpx.AsyncClient() as client:
        await client.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage", json={"chat_id": cid, "text": rep, "parse_mode": "HTML"})
    return "ok"

if TG_TOKEN:
    app.add_url_rule(f'/{TG_TOKEN}', view_func=telegram, methods=['POST'])

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)

