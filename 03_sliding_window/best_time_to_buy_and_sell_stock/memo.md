# Best Time to Buy and Sell Stock

## 💡 最初の考察
- 素直に行くとi日目の株価, i+1日目, i+2..目で愚直に利益を出して最大値を更新していく感じ?
  - ただし、forの2重ループでいく場合内側のループで条件を考慮して飛ばさないといけない
    - 日が進むにつれて,過去は辿れないから範囲が狭まっているのか
     -> TimeLimit Exceeded


## 🤖 AI分析 & フィードバック

**💡 ヒント**
- ある日に売ると決めたとき、利益を最大化するには**その日までの最安値**で買えばいい。
- 配列を左から走査しながら、**今まで見た中での最安値**を1つの変数で記録し続ける。
- 各日について `prices[i] - min_buy_price` が「その日に売った場合の最大利益」。これらの最大値が答え。

**❌ `min()` を1回呼ぶだけではダメな理由**
- `min()` だと配列全体の最安値が出るが、売る日ごとに「それより前の最安値」は変わる。
- 毎回 `min()` で求めると $O(N^2)$ になるので、走査しながら変数で更新していく。

**⚠️ 初期値の注意**
- `min_buy_price = 0` だと、どの価格も0より高いので一度も更新されない。
- `prices[0]` か `float("inf")` にする。

## ✅ 修正後のコード（最適解）
```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_buy_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            current_stock_price = prices[i]
            if current_stock_price < min_buy_price:
                min_buy_price = current_stock_price

            current_profit = current_stock_price - min_buy_price
            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
```

- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(1)$

## 🧠 この解法に辿り着くための思考回路

- **過去を毎回探し直すのではなく、走査しながら記録しておく**
    - 「今の要素に対して、過去の最適な値を参照したい」→ 変数やハッシュマップで追跡する。
    - Two Sum: 過去に見た数字を**ハッシュマップ**で追跡 → O(1) で相方を探す
    - この問題: 過去の最安値を**変数**で追跡 → O(1) で最大利益を計算
    - 共通パターン: **2重ループの内側を、過去の記録で置き換える → $O(N^2)$ → $O(N)$**
