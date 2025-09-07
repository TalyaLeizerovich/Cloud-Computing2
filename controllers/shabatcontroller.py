from models.shabatmodel import callHebCal

async def getShabatInfo():
    answer = await callHebCal()
    return answer
