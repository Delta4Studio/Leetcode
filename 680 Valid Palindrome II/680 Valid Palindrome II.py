 
[table width=98% cellspacing=1 border=1][tr][td bgcolor=#1e1e1e][font=Courier New][size=2][color=#dcdcdc][color=#b8d7a3][color=#569cd6]class[/color] [color=#dcdcdc]Solution[/color]:[/color]
    [color=#dcdcdc][color=#569cd6]def[/color] [color=#dcdcdc]validPalindrome[/color][color=#dcdcdc](self, s)[/color]:[/color]
        [color=#d69d85]"""
        :type s: str
        :rtype: bool
        """[/color]
        
        [color=#d69d85]"""變數設定: 左右指標"""[/color]
        l = [color=#b8d7a3]0[/color]
        r = len(s)[color=#b8d7a3]-1[/color]
        
        [color=#d69d85]"""判斷是否可以產生回文"""[/color]
        [color=#d69d85]"""第一次判斷"""[/color]
        l, r, b = self.fun1(l, r, s)
        [color=#569cd6]if[/color] b:
            [color=#569cd6]return[/color] [color=#569cd6]True[/color]
        [color=#d69d85]"""第二次判斷"""[/color]
        [color=#569cd6]return[/color] self.fun1(l+[color=#b8d7a3]1[/color], r, s)&#91;[color=#b8d7a3]2[/color]&#93; [color=#569cd6]or[/color] self.fun1(l, r[color=#b8d7a3]-1[/color], s)&#91;[color=#b8d7a3]2[/color]&#93;
        
        
    [color=#dcdcdc][color=#569cd6]def[/color] [color=#dcdcdc]fun1[/color][color=#dcdcdc](self, l, r, s)[/color]:[/color]
        [color=#569cd6]while[/color](l < r):
            [color=#569cd6]if[/color](s&#91;l&#93; != s&#91;r&#93;):
                [color=#569cd6]return[/color] l, r, [color=#569cd6]False[/color]
            l += [color=#b8d7a3]1[/color]
            r -= [color=#b8d7a3]1[/color]
        [color=#569cd6]return[/color] l, r, [color=#569cd6]True[/color]
    
[color=#d69d85]"""Min 180ms"""[/color][/size][/font][/td][/tr][/table]
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """變數設定: 左右指標"""
        l = 0
        r = len(s)-1
        
        """判斷是否可以產生回文"""
        """第一次判斷"""
        l, r, b = self.fun1(l, r, s)
        if b:
            return True
        """第二次判斷"""
        return self.fun1(l+1, r, s)[2] or self.fun1(l, r-1, s)[2]
        
        
    def fun1(self, l, r, s):
        while(l < r):
            if(s[l] != s[r]):
                return l, r, False
            l += 1
            r -= 1
        return l, r, True
    
"""Min 180ms"""
