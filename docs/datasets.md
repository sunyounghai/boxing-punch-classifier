# Dataset Survey

## BoxingVI

| 항목 | 내용 |
|---|---|
| arXiv | [arXiv:2511.16524](https://arxiv.org/abs/2511.16524) |
| GitHub | [Bikudebug/BoxingVI](https://github.com/Bikudebug/BoxingVI) |
| 논문 기재 규모 | 6,915 clips / 20 videos / 18 athletes |
| 실제 확보 데이터 | V1~V10 (Google Drive 공유 폴더 기준) |
| 제공 형식 | Annotations (XLSX), Skeleton data (NPY), RGB videos |
| 확인 필요 | 논문에 기재된 데이터셋과 확보한 데이터셋 규모 차이 |

### 확보 데이터 집계 (V1~V10)

| 항목 | 내용 |
|---|---|
| 총 클립 | 5,451 (논문 6,915의 약 79%) |
| 클래스 | Cross 1,371 / Jab 1,287 / Lead Hook 1,035 / Lead Uppercut 687 / Rear Uppercut 679 / Rear Hook 392 |
| 주의 | V6은 NPY가 영상 전체 프레임 단위(클립 분할 필요), V6에 Jab·Cross 없음, V2에 Rear Hook 없음 |
| 이상치 | 끝<시작 5건 |