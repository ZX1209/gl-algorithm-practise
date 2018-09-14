num = input()

# zheng = "整"
# bigNum = ["壹","贰","叁","肆","伍","陆","柒","捌","玖"]
# bigRule = ["圆","拾","佰","仟","万",]


dotPos = num.find(".")

def parseInt(nstr):
    nstr = nstr[::-1]
    ans = []

    bigNum = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
    bigWei = ["圆","万","忆"]
    bigFu = ["","拾","佰","仟"]

    l = len(nstr)
    wei = 0
    cur = 0
    i = 0 

    while i<4 and cur<l:

        ans.append(bigWei[i])

        j = 0
        wei = 0
        while cur<l and j<4:
            if nstr[cur] != '0':
                ans.append(bigFu[wei])
                wei+=1

                ans.append(bigNum[int(nstr[cur])])
                cur+=1

                j+=1
            else:
                if ans[-1] != "零":
                    ans.append("零")
                # 略过 0
                while cur<l and j<4 and nstr[cur]=='0':
                    cur += 1
                    wei+=1
                    j += 1
        i += 1
    return "".join(ans[::-1])

def parseDig(nstr):
    bigNum = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
    bigRule = ["角","分","毫","厘"]
    i = 0
    wei = 0

    ans = []
    while i<len(nstr) and wei < 4:
        ans.append(bigNum[int(nstr[i])])
        ans.append(bigRule[wei])
        wei+=1
        i+=1

    return "".join(ans)



if dotPos == -1:
    tmp = parseInt(num)
    print(tmp+"整")
else:
    tmpInt = parseInt(num[:dotPos])
    tmpDIg = parseDig(num[dotPos+1:])
    print(tmpInt,tmpDIg)

# java version
# import java.io.*;
# import Integer;
# class test  
# {
#     public static void parseint(String nstr)
#     {
#        int i=1;
#     }
    
#     public static String parsedig(String nstr)
#     {
#         String[] bigNum = {"零","壹","贰","叁","肆","伍","陆","柒","捌","玖"};
#         String[] bigRule = {"角","分","毫","厘"};
 
#         int i = 0;
#         int wei = 0;
        
#         String[] ans = new String[100];
#         int ansi = 0;
        
#         while(i<nstr.length() && wei < 4)
#         {
#             int pi = Integer.parseInt([nstr[i]+""]);
#             ans[ansi++] = bigNum[pi];
#             ans[ansi++] = bigRule[wei];
#             wei+=1;
#             i+=1;
#         }
        
#         String tmp = "";
        
#         for(String ts:ans)
#         {
#             if( ts == "")
#             {
#                 break;
#             }
#             else
#             {
#                 tmp = tmp+ts;
#             }
#         }
#         return tmp;
#     }
    
    
#     public static void main (String[] args) throws java.lang.Exception
#     {
       
#         // 使用 System.in 创建 BufferedReader
#         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
#         String str;
#         str = br.readLine();
        
#         int dotPos = str.indexOf('.');
        
        
        
#         if(dotPos == -1)
#         {
#             System.out.println("no .");
#         }
#         else
#         {
#             System.out.println(".");
#         }
        
#         String tmpo = parsedig(str);
        
#         System.out.println(tmpo);
#     }
# }