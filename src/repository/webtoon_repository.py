import pymysql

    # categoryId = 1
    # webtoons = [
    #     {
    #         "title": "똑 닮은 딸",
    #         "author": "이담"
    #     },
    #     {
    #         "title": "신의 탑",
    #         "author": "SIU"
    #     }
    # ]
    #
    # # 방법 1
    # values = ""
    # for webtoon in webtoons:
    #     value = f"(default,\'{webtoon['title']}\',\'{webtoon['author']}\',{categoryId}), "
    #     values += value
    # values = values[:-2]
    # print(values)
    # #(default, '똑 닮은 딸', '이담', 1), (default, '신의 탑', 'SIU', 1)
    #
    #
    # # 방법 2
    # def convert(webtoon: dict, categoryId:int):
    #     return f"(default,\'{webtoon['title']}\',\'{webtoon['author']}\',{categoryId})"
    #
    # values = ""
    # i = 0
    # for webtoon in webtoons:
    #     values = convert(webtoon, categoryId)
    #     if i != len(webtoons) - 1:
    #         values += ", "
    #     i += 1
    # print(values)
    #
    # # 방법 3
    # values = ""
    # valueList = []
    # for webtoon in webtoons:
    #     valueList.append(convert(webtoon, categoryId))
    # print(", ".join(valueList))
    #
    # # 방법 4
    # cv = lambda webtoon: f"(default,\'{webtoon['title']}\',\'{webtoon['author']}\',{categoryId})"
    # valueList = list(map(cv, webtoons))
    # values = ", ".join(valueList)
    # print(values)
    #
    # # 방법 5
    # values = ",".join(list(map(lambda webtoon: f"(default,\'{webtoon['title']}\',\'{webtoon['author']}\',{categoryId})", webtoons)))


def save(webtoonDataList: list):
    for webtoonData in webtoonDataList:
        print(webtoonData)
        newCategoryId = saveCategory(webtoonData['categoryName'])

        for webtoon in webtoonData['webtoons']:
            saveWebtoon(webtoon)

def saveCategory(categoryName: str):
    categoryId = 0
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='Cielo981011', db='naver_webtoon_db')
        try:
            cursor = connection.cursor()
            # sql = f"insert into category_tb values(default, \'{categoryName}\')"
            # cursor.execute(sql)
            sql = "insert into category_tb values(default, %s)"
            cursor.execute(sql, categoryName)
            connection.commit()
            categoryId = cursor.lastrowid
        except Exception as e:
            print(e)
        finally:
            connection.close()
    except Exception as e:
        print("데이터베이스 연결 실패")

        return categoryId

def saveWebtoon(webtoonDict: dict, categoryId: int):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='Cielo981011:)', db='naver_webtoon_db')
        try:
            cursor = connection.cursor()
            sql = f"insert into webtoon_tb values(default, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (webtoonDict['title'], webtoonDict['author'], webtoonDict['rating'], webtoonDict['imgUrl'], categoryId))
            connection.commit()

        except Exception as e:
            print(e)
        finally:
            connection.close()
    except Exception as e:
        print("데이터베이스 연결 실패")


def saveAuthor(webtoonDataList: list):

    authorList = []
    authorSet = set()
    for webtoonData in webtoonDataList:
        for webtoon in webtoonData['webtoons']:
            authorSet.update(webtoon['author'].split(" / "))
    authorList = list(authorSet)
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='Cielo981011:)', db='naver_webtoon_db')
        try:
            cursor = connection.cursor()
            values = ",\n".join(list(map(lambda author: f"(default, \'{author}\')", authorList)))
            sql = f"insert into author_tb values" + values
            cursor.execute(sql)
            connection.commit()

        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")



def saveWebtoonDataList(webtoonDataList: list):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='Cielo981011:)', db='naver_webtoon_db')
        try:
            cursor = connection.cursor()
            for data in webtoonDataList:
                sql = "insert into category_tb values(default, %s)"
                cursor.execute(sql, data["categoryName"])
                category_id = cursor.lastrowid

                values = ",\n".join(list(map(lambda webtoon: f"(default, \'{webtoon['title']}\', \'{webtoon['author']}\', {webtoon['rating']}, \'{webtoon['imgUrl']}\', {category_id})", data['webtoons'])))
                sql = "insert into webtoon_tb values" + values
                cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")
