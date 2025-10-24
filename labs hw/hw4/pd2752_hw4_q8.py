def flat_list(nested_lst,low,high):
    def instance_check_helper(item):
        if not isinstance(item,list):
            return [item]
        result=[]
        for i in item:
            result+=instance_check_helper(i)
        return result
    if low>high:
        return []
    return instance_check_helper(nested_lst[low])+flat_list(nested_lst,low+1,high)

nested_lst=[[1,2],3,[4,[5,6,[7],8]]]
print(flat_list(nested_lst,0,len(nested_lst)-1))