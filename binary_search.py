def binary_search(arr,ele):
    first=0
    last=len(arr)-1
    found=False
    while first<=last and not found:
        mid=(first+last)//2


        if arr[mid]==ele:
            found=True
        else:
            if ele<arr[mid]:
                last=mid-1
            elif ele>arr[mid]:
                first=mid+1
    return found


#print(binary_search([1,2,3],4))

def test_case():
    arr = [1,2,3,4,5,6,7,8,9,10]
    assert binary_search(arr,4)==True
    assert binary_search(arr,3)==True
    assert binary_search(arr,10)==True
    assert binary_search(arr,13)==False



if __name__=="__main__":
    test_case()
