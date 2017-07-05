class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        left=x
        right=x
        up=y
        down=y
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]=="1":
                    left=min(i,left)
                    right=max(i,right)
                    up=min(j,up)
                    down=max(j,down)

        return (down-up+1) * (right-left+1)    ###The brute force is too time consuming





# 00001001001
# 11000011111
# 11111111111
# 00000000000
# 00000000000


class Solution2(object):



    def minArea(self,image,x,y):
        top=self.searchRows(image,0,x,True)
        bottom=self.searchRows(image,x+1,len(image),False)
        left=self.searchColumns(image,0,y,top,bottom,True)
        right=self.searchColumns(image,y+1,len(image[0]),top,bottom,False)


        return (bottom-top)*(right-left)



    def searchColumns(self,image,i,j,top,bottom,opt):
        while i!=j:
            mid=(i+j)//2
            if any(image[k][mid]=="1" for k in range(top,bottom))==opt:
                j=mid
            else:
                i=mid+1
        return i






    def searchRows(self,image,i,j,opt):
        while i!=j:
            mid=(i+j)//2
            if ("1" in image[mid])==opt:
                j=mid
            else:
                i=mid+1
        return i
