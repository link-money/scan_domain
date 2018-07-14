# encoding:utf-8

# 这是一个域名查询的小程序

def inquire_domain(domain_name):
    '''

    :param domain_name: 域名，字符串，无须www，例如：link.link
    :return: True 或者 False， 字面意思
    '''

    import requests

    url='http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='
    html = requests.get(url+domain_name)
    content=html.text
    if 'Domain name is available' in content:
        print(domain_name)
        return True
    elif 'illegal' in content.lower():
        print(domain_name+'illegal')
    else:
        return False


if __name__=='__main__':
    import threading
    # 域名尾椎：
    suffices=list(set('com.cn.xin.net.top.在线.xyz.wang.shop.site.club.cc.fun.online.biz.red.link.ltd.mobi.info.org.com.cn.net.cn.org.cn.gov.cn.name.vip.pro.work.tv.co.kim.group.tech.store.ren.ink.pub.live.wiki.design.中文网.我爱你.中国.网址.网店.公司.网店.集团..cc  .shop  .vip  .club  .网址  .ltd  .网店  .xyz .top  .在线  .手机  .中文网  .site  .wang  .link  .net .com.cn  .red  .pro  .集团  .中国  .公司  .企业  .网络 .biz  .mobi  .info  .ink  .online  .store  .tech  .org     .name  .auto  .ren  .我爱你 .love  .work  .fun  .run  .chat  .gold  .plus  .team .show  .world  .group  .center  .social  .video  .cool  .zone .today  .city  .company  .live  .fund  .guru  .pub  .email .life  .wiki  .design'.replace(' ','').split('.')))

    names='money,jin,gold'.split(',')
    domain_names=[]
    for name in names:
        for suffix in suffices:
            domain_names.append(name+'.'+suffix)


    j=0
    while j<len(domain_names)-5:
        threads = []
        for i in range(j,j+5):
            # print(domain_names[i])
            thread=threading.Thread(target=inquire_domain,args=(domain_names[i],))
            threads.append(thread)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        j+=5


    # inquire_domain('link.link')
