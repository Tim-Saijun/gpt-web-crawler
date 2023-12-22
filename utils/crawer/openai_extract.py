from openai import OpenAI
from config import openai_config
import logging
client = OpenAI(
    # api_key=os.environ.get("OPENAI_API_KEY"),
    base_url = openai_config["base_url"],
    api_key = openai_config["token"]
)

def openai_extract(meta_info,c_data):
    json_format = str({"prodName":" ","prodBrief": " ","productKeyword": " ","productCategory": " ","ProductFeatures": " ","prodAttribute": " ","productText": " ","prodImg": " "})
    json_format1 = str({"content":""})
    p3 = f"下面给出的文本是来自一个网页，可能是产品描述或其它内容。请根据{meta_info}判断，如果是产品页，则提取产品信息填充json{json_format},最终返回此json即可；如果不是产品页面，则提取相关的正文内容，填充json{json_format1}。无论如何，最后返回的一定是json格式，要处理的文本如下："
    p4 = f"下面给出的文本是来自一个网页，可能是产品描述或其它内容。请根据{meta_info}判断，如果是产品页，则提取产品信息填充json{json_format},最终返回此json即可；如果不是产品页面，则提取相关的正文内容，填充json{json_format1}。无论如何，最后返回的一定是标准的json格式，不需要额外的解释或代码渲染。要处理的文本如下："
    prompt = p4
    content = prompt + c_data
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            # model="gpt-3.5-turbo-1106",
            model="gpt-4-1106-preview",
            response_format={ "type": "json_object" },
            temperature=0,
            timeout=120,
        )
    except:
        logging.warning("openai请求失败")
        return str({"content":""}),0
    tokens_used = chat_completion.usage.total_tokens if chat_completion.usage is not None else 0
    return chat_completion.choices[0].message.content,tokens_used
if __name__ == '__main__':
    meta_info = "标题：油烟机 - 浙江捷昌线性驱动科技股份有限公司，关键词：油烟机, 浙江捷昌线性驱动科技股份有限公司，简介：油烟机，浙江捷昌线性驱动科技股份有限公司"
    c_data = " 汉堡 关闭 简体中文 路径 首页 产品 部件 系统 商城 部件 电动推杆 升降立柱 遮阳驱动 伺服电机 控制器 操作器 配件 系统 升降桌系统 可调节床架 升降电视机架 洗澡椅 升降坐便器 升降吊柜 升降梳妆台 台面平移 电动轮椅 商城 业务领域 智慧办公 医疗康护 智能家居 工业自动化 智慧办公 TF组合工位 TT组合工位 TS单人工位 TO单人工位 高级办公桌 主管桌 Odette会议桌 升降白板 升降讲台 工作舱 Zen新中式升降桌 升降茶几 居家升降桌 蜂窝板升降桌 电竞升降桌 儿童学习桌 医疗康护 电动病床 影像设备 检查床/诊疗床 手术床 婴儿培育箱 家用护理床 移位器 电动轮椅 升降坐便器 洗澡椅 沐浴床 眼科检查台 治疗椅 理容椅 牵引床 按摩床 OT训练设备 直立床 康复机器人 智能家居 升降吊柜 升降岛台 升降电视机架 升降衣柜 升降梳妆台 升降梳妆镜 电竞升降桌 Zen 新中式升降桌 儿童学习桌 油烟机 洗碗机 可调节床架 遮阳驱动 工业自动化 光伏应用 光热应用 建筑工程机械 环卫车辆 AGV/物流叉车 石油设备（防爆） 扫地机器人 关于捷昌 捷昌简介 捷昌优势 捷昌文化 捷昌年刊 社会责任 行为守则 可持续发展 检测实力 捷昌简介 捷昌优势 捷昌文化 捷昌年刊 社会责任 行为守则 可持续发展 检测实力 服务 满意度调查 升降系统定制 常见问题 相关下载 满意度调查 升降系统定制 常见问题 相关下载 新闻中心 新闻资讯 视频浏览 新闻资讯 视频浏览 联系我们 全球办事处 投资者关系 加入我们 合作伙伴 全球办事处 投资者关系 加入我们 合作伙伴 简体中文 简体中文 Pусский 日本語 Deutsch Español English हिन्दी 搜索 路径 家电驱动 油烟机 烟机风门开启系统——人体感应，手臂一挥，即可轻松开启烟机风门智能的操作让生活更简单智能操作开启油烟机风门，无需触碰，通过人体感应，只要手臂轻轻一挥就可开启产品经久耐用，高标准，高品质适用在油烟机上面的产品除了精美小巧、结构紧凑，噪音低之外，还需要产品经久耐用，JIECANG的产品都经过严格的测试，以确保产品的品质达标，减少维护次数，延长使用寿命。​​​​​​​​​​​​​​ 查看更多 下拉箭头小 收起箭头 电动推杆 JC35N1 查看更多 电动推杆 JC35L19 查看更多 电动推杆 JC35N1 查看更多 电动推杆 JC35L19 查看更多 相关产品 油烟机 JC35N1 · 最大负载：50N · 防护等级：IP54 · 直线型推杆，尺寸小巧 油烟机 JC35N · 最大负载：20N · 防护等级：最高可达IPX6 · 直线型推杆，尺寸小巧 油烟机 JC35L19系列 · 最大负载：100N · 防护等级：IP20 · 直线型推杆，尺寸小巧 视频 相关应用 查看更多 查看更多 查看更多 分组 3 Created with Sketch. 分组 3 copy Created with Sketch. 探索与发现 智能家居 建博会今日启幕！捷昌智能驱动，演绎智慧人居空间 捷昌全屋智能家居驱动系统，致力于打造理想生活方式整体解决方案，将舒适、便捷、智慧、有序融入居家空间。 智能家居 捷昌驱动赋能厨卫空间产品智能化升级 2021年5月26日-29日，第26届中国国际厨房、卫浴设施展览会（KBC 2021）在上海新国际博览中心举行。该展会历来被视作厨卫行业发展的风向标。 智能家居 开启智能家居新生活｜捷昌驱动亮相中国建博会（广州） 开启智能家居新生活｜捷昌驱动亮相中国建博会（广州） 快速链接 快速导航 首页 部件 系统 业务领域 关于捷昌 服务 新闻资讯 联系我们 部件 快速导航 电动推杆 升降立柱 遮阳驱动 伺服电机 控制器 操作器 配件 400-6666-358 jc35@jiecang.com 留言 2355502916 系统 快速导航 升降桌系统 可调节床架 升降电视机架 洗澡椅 升降坐便器 升降吊柜 升降梳妆台 台面平移 电动轮椅  地址：浙江省新昌县省级高新技术产业园区莱盛路2号  电话：400-6666-358 https://weibo.com/p/1006063675752922/home?from=page_100606&mod=TAB#place 版权所有  2022 浙江捷昌线性驱动科技股份有限公司 站点地图 | 隐私政策 浙ICP备11031253号-8 "
    res = openai_extract(meta_info,c_data)
    print(res)