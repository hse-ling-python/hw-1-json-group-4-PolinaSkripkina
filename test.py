import json
from collections import Counter

# 1. Считаем количество строк в файле как длину списка.
tweets = []
for line in open('hw_3_twitter.json'):
    tweets.append(json.loads(line))
print(len(tweets))

# 2. Считаем количество удаленных твитов, проверяя, помечены ли они как 'delete', и считаем их долю от всех твитов.
deleted = 0
for tweet in tweets:
    if 'delete' in tweet:
        deleted += 1
percentage_of_deleted = deleted / len(tweets) * 100
print(str(percentage_of_deleted) + '%')

# 3. С помощью Counter создаем частотный словарь языков, после чего выводим 10 свмых частотных из них.
c = Counter()
for tweet in tweets:
    if 'lang' in tweet:
        c += Counter(tweet['lang'].split())
print(*c.most_common(10))
c.clear()

# 4. С помощью Counter создаем частотный словарь имен пользователей, затем
for tweet in tweets:
    if 'user' in tweet:
        c += Counter(tweet['user']['id_str'].split())
n = 0 # количество пользователей с несколькими твитами
for key, value in c.items():
    if value > 1:
        n += 1
print(n)
c.clear()

# 5. С помощью Counter создаем частотный словарь хэштэгов, затем выводим 20 самых частотных.
for tweet in tweets:
    if 'entities' in tweet:
        for hashtag in tweet['entities']['hashtags']:
            if 'text' in hashtag:
                c += Counter(hashtag['text'].split())
print(*c.most_common(20))
c.clear()

