'''
面试题 16.08. 整数的英语表示
给定一个整数，打印该整数的英文描述。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

'''
UNITS = ['', 'One', 'Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
         'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TENS = [None, None, 'Twenty', 'Thirty', 'Forty', 'Fifty',
        'Sixty', 'Seventy', 'Eighty', 'Ninety']


class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return 'Zero'
        billion = num // 1000000000
        num %= 1000000000
        million = num // 1000000
        num %= 1000000
        thousand = num // 1000
        num %= 1000

        def three(num):
            if num < 20:
                return UNITS[num]
            elif num < 100:
                res = TENS[num // 10]
                remains = num % 10
                if remains:
                    res += ' ' + UNITS[remains]
                return res
            else:
                res = UNITS[num // 100] + ' ' + 'Hundred'
                remains = num % 100
                if remains:
                    res += ' ' + three(remains)
                return res

        res = []
        if billion:
            res.append(self.numberToWords(billion))
            res.append('Billion')
        if million:
            res.append(three(million))
            res.append('Million')
        if thousand:
            res.append(three(thousand))
            res.append('Thousand')
        if num:
            res.append(three(num))
        return ' '.join(res)
