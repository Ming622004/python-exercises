"""
之前面試的題目，那時寫的不是很好
將詞的字以樹狀結構寫出來，0代表詞沒完結，1代表詞完結
input: 命理師,命運,命運女神,上海,上海海水
output:
命:0
  理:0
    師:1
  運:1
    女:0
      神:1
上:0
  海:1
    海:0
      水:1
"""


class WordNode:
    def __init__(self, word, layer, front):
        self.word = word
        self.end_check = False
        self.layer = layer
        self.front = front
        self.behind = []

    # 印出來全部(root不印) 會往下一層找
    def print_all(self):
        if self.word:
            print("%s%s:%d" % ("  "*(self.layer-1), self.word, int(self.end_check)))
        if len(self.behind):
            for node in self.behind:
                node.print_all()

    def word_in_check(self, word_s):
        word_next = []
        for node_next in self.behind:
            word_next.append(node_next.word)
        return word_s in word_next


def main():
    word_input = "命理師,命運,命運女神,上海,上海海水"
    word_list = word_input.split(",")

    node_root = WordNode(None, 0, None)

    for word in word_list:
        node_now = node_root
        while not word == "":
            word, word_in = word[1:], word[0]
            # 如果字沒在下一層就加node到behind
            if not node_now.word_in_check(word_in):
                node_now.behind.append(WordNode(word_in, node_now.layer + 1, node_now))

            # 找出下個字的node變成node_now
            for node_next in node_now.behind:
                if node_next.word == word_in:
                    node_now = node_next
                    break
        # 最後一個字
        node_now.end_check = True

    # 印出來看結果
    node_root.print_all()


if __name__ == '__main__':
    main()




