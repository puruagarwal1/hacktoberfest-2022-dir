//Given a roman numeral, convert it to an integer.

class RomanToInt {
    public int romanToInt(String s) {
        HashMap<Character,Integer> map = new HashMap();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
        
        char[] stringList = s.toCharArray();
        
        if(s.length()==1) return map.get(stringList[0]);
        
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            int num = map.get(stringList[i]);
            
            
            if((i + 1) < s.length() && (num < map.get(stringList[i+1]))){
                int behind = num;
                int ahead =map.get(stringList[i+1]);
                if(behind == 1 && (ahead ==5 || ahead == 10)) sum -= num;
                else if(behind == 10 && (ahead ==50 || ahead == 100)) sum -= num;
                else if(behind == 100 && (ahead ==500 || ahead == 1000)) sum -= num;
                else  sum += num;
            }
            else sum += num;

            
            System.out.println("After " + sum);

        }        
        return sum;
        
    }
}
