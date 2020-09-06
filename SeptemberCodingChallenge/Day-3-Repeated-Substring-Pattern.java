class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String t = "";
        int len = s.length();
        for(int x = 0; x < (len / 2); x++){
            t = s.substring(0, x+1);
            int l = t.length();
            for(int y = l; y<=len-l ; y+=l){
                if(s.substring(y, y+l).equals(t)){
                    if(y < (len - l))
                        continue;
                    else
                        return true;}
                else
                    break;}}
        return false;
    }
}
