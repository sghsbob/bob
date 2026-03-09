# 🍱 School Meal Bot (Unified)

[English](#english) | [한국어](#한국어)

---

<a name="english"></a>

A lightweight KakaoTalk/Telegram meal notification bot using the NEIS (National Education Information System) API.  
Structured as a single file and optimized for serverless environments like Vercel.

## 🛠 Required Environment Variables

You must set the following environment variables during deployment:

| Variable         | Description                   | Example         |
| :--------------- | :---------------------------- | :-------------- |
| `NEIS_API_KEY`   | NEIS Open API Key             | `abc123...`     |
| `OFFICE_CODE`    | Education Office Code         | `B10` (Seoul)   |
| `SCHOOL_CODE`    | Standard School Code          | `7010817`       |
| `TELEGRAM_TOKEN` | Telegram Bot Token (Optional) | `123456:ABC...` |

## 🚀 How to Deploy

1. Fork this repository.
2. Connect to Vercel.
3. Configure the environment variables listed above.
4. KakaoTalk Skill URL: `https://your-app.vercel.app/api/kakao`
5. Telegram Webhook URL: `https://your-app.vercel.app/api/telegram`

## ⚖️ License

MIT License. Feel free to use and modify.

---

<a name="한국어"></a>

# 🍱 급식 알리미 (통합 버전)

나이스(NEIS) 급식 API를 활용한 카카오톡/텔레그램 급식 알리미입니다.  
단일 파일로 구성되어 Vercel 등 서버리스 환경에 최적화되어 있습니다.

## 🛠 필수 환경 변수

배포 시 다음 환경 변수를 반드시 설정해야 합니다.

| 변수명           | 설명                            | 예시            |
| :--------------- | :------------------------------ | :-------------- |
| `NEIS_API_KEY`   | 나이스 교육정보 개방포털 API 키 | `abc123...`     |
| `OFFICE_CODE`    | 시도교육청 코드                 | `B10` (서울)    |
| `SCHOOL_CODE`    | 표준학교코드                    | `7010817`       |
| `TELEGRAM_TOKEN` | 텔레그램 봇 토큰 (선택사항)     | `123456:ABC...` |

## 🚀 배포 방법

1. 본 저장소를 Fork 합니다.
2. Vercel에 연결합니다.
3. 상기 환경 변수를 설정합니다.
4. 카카오톡 스킬 URL: `https://your-app.vercel.app/api/kakao`
5. 텔레그램 웹훅 URL: `https://your-app.vercel.app/api/telegram`

## ⚖️ 라이선스

MIT License. 누구나 자유롭게 수정 및 배포가 가능합니다.
