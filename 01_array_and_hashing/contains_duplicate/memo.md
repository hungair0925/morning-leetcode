# Contains Duplicate

## 💡 最初の考察
- 順当にやれば、2重ループ
- 1回値を舐めながら、value: indexの辞書を作ればいけそう

## ✅ 解いたコード

- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$
- [Two Sum](https://zenn.dev/hungair0925/articles/45705f609ab93c)と同じく、ハッシュマップで「過去に見たか」を追跡する
- 同じ値が出た時点で即 `True` を返す

## 🤖 AIレビュー

この問題はインデックスが不要なので、`dict` より `set` の方がシンプル。

```python
def hasDuplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False
```

一行でも書ける。

```python
def hasDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
```

ただし `dict` での解法は間違いではない。`set` は「存在確認だけしたい」ときの道具の選択の話。

---

## 🧠 この解法に辿り着くための思考回路

- **「過去に見たか」を記録したい → ハッシュマップ（or セット）**
    - Two Sumと同じパターン。「過去の記録を使って2重ループを省く」
    - インデックスが必要 → `dict`、存在確認だけでいい → `set`
