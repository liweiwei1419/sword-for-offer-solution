/**
 * @author liwei
 * @date 18/6/14 上午9:21
 */
public class Solution2 {

    public String replaceSpace(StringBuffer str) {
        return str.toString().replaceAll("\\s", "%20");
    }
}
