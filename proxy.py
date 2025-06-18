import asyncio
import time

class ProxyManager:

    def __init__(self, timeout: int = 2) -> None:
        proxies_list = [
            "http://SGvq8W:U4yiBi1Uzw@185.181.246.95:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.204.162:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.205.48:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.143.59:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.128.60:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.166.123:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.220.116:3000",
            "http://SGvq8W:U4yiBi1Uzw@194.34.248.5:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.81.137.8:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.84.177.35:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.56.96:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.11.11:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.11.141:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.167.226:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.221.15:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.49.49:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.139.127:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.189.153:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.184.93:3000",
            "http://SGvq8W:U4yiBi1Uzw@95.182.124.71:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.23.140:3000",
            "http://SGvq8W:U4yiBi1Uzw@212.115.49.114:3000",
            "http://SGvq8W:U4yiBi1Uzw@92.119.193.44:3000",
            "http://SGvq8W:U4yiBi1Uzw@5.183.130.104:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.11.20.191:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.15.72.143:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.15.73.195:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.81.136.33:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.81.136.83:3000",
            "http://SGvq8W:U4yiBi1Uzw@45.81.137.151:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.142.83:3000",
            "http://SGvq8W:U4yiBi1Uzw@185.181.245.72:3000",
            "http://SGvq8W:U4yiBi1Uzw@185.181.245.139:3000",
            "http://SGvq8W:U4yiBi1Uzw@185.181.247.102:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.204.251:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.16.52:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.143.75:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.143.227:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.15.37:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.142.54:3000",
            "http://SGvq8W:U4yiBi1Uzw@185.181.245.20:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.136.2:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.110.90:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.110.248:3000",
            "http://SGvq8W:U4yiBi1Uzw@109.248.13.38:3000",
            "http://SGvq8W:U4yiBi1Uzw@188.130.129.44:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.22.27:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.22.98:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.23.80:3000",
            "http://SGvq8W:U4yiBi1Uzw@46.8.23.87:3000"]

        self.proxies = {proxy: 0 for proxy in proxies_list}
        self.timeout = timeout
        self.locks = {proxy: asyncio.Lock() for proxy in self.proxies} 
        self.queue = asyncio.PriorityQueue()
        for proxy in self.proxies:
            self.queue.put_nowait((0, proxy))

    async def get_proxy(self) -> str:
        while True:
            curr_time = time.time()
            last_used, proxy = await self.queue.get()
            if last_used <= curr_time:
                async with self.locks[proxy]:
                    if self.proxies[proxy] <= time.time():
                        self.proxies[proxy] = time.time() + self.timeout
                        self.queue.put_nowait((self.proxies[proxy], proxy))  
                        return proxy
            
            wait_time = last_used - curr_time
            if wait_time > 0:
                await asyncio.sleep(wait_time)
            self.queue.put_nowait((last_used, proxy))
