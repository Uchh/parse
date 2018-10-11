class pars:
    def poisk(self):
        from contextlib import suppress
        import requests, bs4
        s = requests.get('https://vk.com/id239469227')
        b = bs4.BeautifulSoup(s.text, "html.parser")
        zapis = ""
        with suppress(Exception):
            fl_l = b.select('.pp_status')
            infa = fl_l[0].getText()
            print("Статус: ", infa)
            zapis+=infa+" "
        with suppress(Exception):
            fl_2 = b.select('title')
            infa2 = fl_2[0].getText()
            print("Имя и фамилия: ", infa2)
            zapis += infa2+" "
        with suppress(Exception):
            fl_3 = b.select('.pp_info')
            infa3 = fl_3[0].getText()
            print("Откуда? Сколько лет? ", infa3)
            zapis += infa3+" "
        with suppress(Exception):
            fl_4 = b.select('.pp_last_activity_text')
            infa4 = fl_4[0].getText()
            print("Когда был(а) в сети? ", infa4)
            zapis += infa4+" "
        with suppress(Exception):
            fl_5 = b.select('.pm_item .pm_counter')
            infa5 = fl_5[0].getText()
            print("Количество фотографий? ", infa5)
            zapis += infa5+" "
        with suppress(Exception):
            fl_6 = b.select('dd')
            infa6 = fl_6[0].getText()
            print("Дата рождения? ", infa6)
            zapis += infa6+'\n'
        return zapis


if __name__ == "__main__":
    pars = pars()
    pars1 = pars.poisk()
    pars2 = open('вк.txt','a')
    pars2.write(pars1)
    pars2.close()
