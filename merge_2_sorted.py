def mergeSortedArray( A, m, B, n):
        # write your code here
        i=0
        j=0
        results=[]
        while i<m and j<n:
            if A[i] < B[j]:
                results.append(A[i])
                i+=1
            else:
                results.append(B[j])
                j+=1

        while i<m:
            results.append(A[i])
            i+=1

        while j<n:
            results.append(B[j])
            j+=1



        return results

print(mergeSortedArray([1,2,3],3,[4,5],2))
