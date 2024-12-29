### verify memory consumption

- claude-3-haiku-20240307

```
your question: 東京駅のおすすめグルメを3つ教えてください。

Claude: はい、東京駅周辺のおすすめグルメをいくつか紹介します。

1. 東京ラーメンストリート
東京駅構内にある「東京ラーメンストリート」は、さまざまなラーメン店が集まる人気のスポットです。有名店の味を気軽に楽しめるのが魅力です。

2. 京橋エドグラン
東京駅の京橋口から少し歩いた場所にある「京橋エドグラン」は、老舗の和食店やカフェなどが集まる高級感のある商業施設です。ランチタイムは特におすすめです。

3. 丸の内 KITTE
東京駅の丸の内側にある「丸の内 KITTE」は、さまざまなグルメが集まる複合商業施設です。和食、洋食、カフェなど、様々なジャンルの美味しい店が揃っています。

いかがでしょうか。東京駅周辺には美味しいグルメがたくさんありますので、時間があれば色々と歩いて探してみるのも良いかもしれません。

Filename: /Users/goayasushi/programming/app/claude_chat/chat.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     51.9 MiB     51.9 MiB           1   @profile
    18                                         def call_claude_api(question):
    19                                             # message create: https://docs.anthropic.com/en/docs/initial-setup
    20     53.6 MiB      1.7 MiB           2       message = client.messages.create(
    21                                                 # claude model: https://docs.anthropic.com/en/docs/about-claude/models
    22     51.9 MiB      0.0 MiB           1           model="claude-3-haiku-20240307",
    23     51.9 MiB      0.0 MiB           1           max_tokens=1000,
    24     51.9 MiB      0.0 MiB           1           temperature=0.7,
    25     51.9 MiB      0.0 MiB           1           messages=[{"role": "user", "content": question}],
    26                                             )
    27
    28                                             # extract answer from response
    29     53.6 MiB      0.0 MiB           2       answer = "".join([block.text for block in message.content])
    30     53.6 MiB      0.0 MiB           1       print(f"\nClaude: {answer}\n")
    31     53.6 MiB      0.0 MiB           1       return answer

```

- claude-3-5-sonnet-20240620

```
your question: 東京駅のおすすめグルメを3つ教えてください。

Claude: 東京駅には多くの美味しい飲食店がありますが、以下の3つのグルメスポットがおすすめです：

1. 東京らーめんストリート：
東京駅の地下1階にある「東京ラーメンストリート」には、日本各地の有名ラーメン店が8店舗集まっています。中でも人気なのは、濃厚な鶏白湯スープが特徴の「竹末東京プレミアム」や、魚介系スープが絶品の「六厘舎」です。

2. 東京駅構内の駅弁売り場：
改札内にある「グランスタ東京」の駅弁売り場では、全国各地の名物駅弁を購入できます。特に「東京弁当」や「まぐろ尽くし」などが人気です。新幹線や電車での旅行前に購入するのがおすすめです。

3. T's たんたん：
東京駅構内にある完全ヴィーガンのラーメン店です。動物性食材を一切使用せず、健康的で美味しいラーメンを提供しています。特に「ごまたんたん麺」が人気メニューです。

これらのスポットは、東京駅を訪れた際に是非立ち寄ってみてください。それぞれ異なる魅力があり、東京駅での食事を楽しむことができます。

Filename: /Users/goayasushi/programming/app/claude_chat/chat.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    17     49.5 MiB     49.5 MiB           1   @profile
    18                                         def call_claude_api(question):
    19                                             # message create: https://docs.anthropic.com/en/docs/initial-setup
    20     51.3 MiB      1.8 MiB           2       message = client.messages.create(
    21                                                 # claude model: https://docs.anthropic.com/en/docs/about-claude/models
    22     49.5 MiB      0.0 MiB           1           model="claude-3-5-sonnet-20240620",
    23     49.5 MiB      0.0 MiB           1           max_tokens=1000,
    24     49.5 MiB      0.0 MiB           1           temperature=0.7,
    25     49.5 MiB      0.0 MiB           1           messages=[{"role": "user", "content": question}],
    26                                             )
    27
    28                                             # extract answer from response
    29     51.3 MiB      0.0 MiB           2       answer = "".join([block.text for block in message.content])
    30     51.3 MiB      0.0 MiB           1       print(f"\nClaude: {answer}\n")
    31     51.3 MiB      0.0 MiB           1       return answer

```
