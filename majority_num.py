def majorityNumber(nums):
        # write your code here
        counter={}
        for num in nums:
            if num not in counter:
                counter[num]=1
            else:
                counter[num]+=1
                # print(counter)
                if counter[num] > (len(nums)/2):
                    return num
        return None



if __name__=="__main__":
    print(majorityNumber([1,1,1,1,2,2,2]))
