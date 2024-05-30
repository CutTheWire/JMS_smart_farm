import pytest
import asyncio
from httpx import AsyncClient
from datetime import datetime, timedelta
import sys
import json
sys.path.append('.\\JMS_smart_farm\\Py\\api')
import complexed_chart
from complexed_chart import app

@pytest.mark.anyio
async def test_black_box():
    '''
    black box test

    get  : /api, /api/latest
    post : /api/week, /api/date, /api/month, /api/hourly
    '''
    
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # GET 요청 테스트
        get_endpoints = ["/api", "/api/latest"]
        for endpoint in get_endpoints:
            response = await ac.get(endpoint)
            assert response.status_code == 200


        # 테스트할 HTTP 상태 코드
        status_codes = [400, 500, 404, 422, 424, 429, 502]
        
        # 각 상태 코드를 테스트하기 위한 POST 요청
        for status_code in status_codes:
            response = await ac.post(f"/example/{status_code}")
            assert response.status_code == status_code
            

        # POST 요청 테스트
        post_endpoints = {
            "/api/date": {"date": "2024-05-16"},
            "/api/hourly": {"date": "2024-05-16"},
            "/api/week": {"year": 2024, "month": 12, "week": 2},
            "/api/month": {"year": 2024, "month": 12},
        }

        for endpoint, data in post_endpoints.items():
            response = await ac.post(endpoint, json=data)
            assert response.status_code == 200

class WhiteTest:
    def __init__(self) -> None:
        self.complexed_chart = complexed_chart
        self.complexed_chart.get_db_connection("JMSPlant_test.db")

    async def __call__(self) -> None:
        self.test_white_week_date()
        self.test_white_week_days()
    
    def test_white_week_date(self) -> None:
        current_date_item = None
        data_item = self.complexed_chart.week_date(year=2024, month=3, week_index=5)
        data_bool = data_item == current_date_item
        print(
            f"{data_bool}\n"
            f"data_item         : {data_item}\n"
            f"current_date_item : {current_date_item}"
        )
        assert data_item == current_date_item

    def test_white_week_days(self) -> None:
        current_date_item = None
        days = 32 # 경계 데이터 테스트
        start_date = datetime.strptime("2024-05-01", "%Y-%m-%d")
        data_item = self.complexed_chart.week_days(start_date, days=days, control=3)
        data_bool = data_item == current_date_item
        print(
            f"{data_bool}\n"
            f"data_item         : {data_item}\n"
            f"current_date_item : {current_date_item}"
            )
        assert data_item == current_date_item

        current_date=[]
        days = 31
        start_date = datetime.strptime("2024-06-30", "%Y-%m-%d") # 경계 날짜 테스트
        for i in range(days):
            current_date.append(str(start_date + timedelta(days=i)))
        data_items = self.complexed_chart.week_days(start_date,
                                                    days=days,
                                                    control=3)
        print("")
        for index, (data_item, current_date_item) in enumerate(zip(data_items, current_date)):
            data_bool = data_item['created_at'] == current_date_item
            print(
                f"{index, data_bool}\n"
                f"data_item['created_at'] : {data_item['created_at']}\n"
                f"current_date_item       : {current_date_item}"
                )
            assert data_item['created_at'] == current_date_item

@pytest.mark.anyio
async def main():
    await test_black_box()

if __name__ == "__main__":
    white_test_instance = WhiteTest()
    asyncio.run(white_test_instance())  # 비동기 호출
    pytest.main()