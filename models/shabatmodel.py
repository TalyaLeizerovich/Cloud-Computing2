import httpx

URL = "https://www.hebcal.com/shabbat?cfg=json&geonameid=281184&M=on"

async def callHebCal():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        return response.json()
