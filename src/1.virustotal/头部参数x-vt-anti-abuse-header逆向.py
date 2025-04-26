import requests
import execjs

js_code = """
function computeAntiAbuseHeader() {
    const e = Date.now() / 1e3;
    return Buffer.from(`${( () => {
        const e = 1e10 * (1 + Math.random() % 5e4);
        return e < 50 ? "-1" : e.toFixed(0)
    }
    )()}-ZG9udCBiZSBldmls-${e}`).toString("base64");
}
"""


x_vt = execjs.compile(js_code).call('computeAntiAbuseHeader')
print(x_vt)

headers = {
    "accept": "application/json",
    "accept-ianguage": "en-US,en;q=0.9,es;q=0.8",
    "accept-language": "zh-CN,zh;q=0.9",
    "content-type": "application/json",
    "priority": "u=1, i",
    "referer": "https://www.virustotal.com/",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-app-version": "v1x384x0",
    "x-tool": "vt-ui-main",
    "x-vt-anti-abuse-header": x_vt
}
cookies = {
    "_gid": "GA1.2.394721794.1745657197",
    "_ga": "GA1.1.1460209426.1742100195",
    "_gat": "1",
    "_ga_BLNDV9X2JR": "GS1.1.1745677157.5.1.1745677943.0.0.0"
}
url = "https://www.virustotal.com/ui/search"
params = {
    "limit": "2",
    "relationships%5Bcomment%5D": "author,item",
    "query": "https://github.com/"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)
