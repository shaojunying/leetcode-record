import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;

/**
 * Created by shao on 2018/10/3.
 */
public class 设计哈希集合 {

    class MyHashSet {
//        此方法用了java内部自带的方法
//
//        private HashMap<Integer,Integer> hashMap;
//
//        /** Initialize your data structure here. */
//        public MyHashSet() {
//            hashMap = new HashMap<>();
//        }
//
//        public void add(int key) {
//            hashMap.put(key, 1);
//        }
//
//        public void remove(int key) {
//            hashMap.remove(key);
//        }
//
//        /** Returns true if this set did not already contain the specified element */
//        public boolean contains(int key) {
//            return hashMap.containsKey(key);
//        }
//        此方法生命一个大数组
        boolean[][] table = new boolean[1000][];
        public MyHashSet() {
        }

        public void add(int key) {
            int temp = key%1000;
            if (table[temp]==null){
                table[temp] = new boolean[1001];
            }
            table[temp][key/1000]=true;
        }

        public void remove(int key) {
            int temp = key%1000;
            if (table[temp]==null){
                table[temp] = new boolean[1001];
            }
            table[key%1000][key/1000]=false;
        }
        public boolean contains(int key) {
            return table[key%1000]!=null && table[key%1000][key/1000];
        }

    }

}
