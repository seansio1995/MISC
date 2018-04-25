def merge_list(mylist,alicelist):
    mergedlist_length=len(mylist)+len(alicelist)
    mergedlist=[None]*mergedlist_length


    # head_of_mylist=mylist[0]
    # head_of_alicelist=alicelist[0]
    #
    #
    # if head_of_mylist < head_of_alicelist:
    #     mergedlist[0]=head_of_mylist
    #
    # else:
    #     mergedlist[0]=head_of_alicelist

    current_index_mine=0
    currect_index_alice=0
    current_index_merged=0


    while current_index_merged < mergedlist_length:
        # first_unmerged_mine=mylist[current_index_mine]
        # first_unmerged_alice=alicelist[currect_index_alice]

        if current_index_mine >= len(mylist):
            mergedlist[current_index_merged]=alicelist[currect_index_alice]      #mylist is exhausted
            currect_index_alice+=1

        elif currect_index_alice >= len(alicelist):
            mergedlist[current_index_merged]=mylist[current_index_mine]          # alicelist is exhausted
            current_index_mine+=1

        elif mylist[current_index_mine] < alicelist[currect_index_alice]:
            mergedlist[current_index_merged]=mylist[current_index_mine]
            current_index_mine+=1

        else:
            mergedlist[current_index_merged]=alicelist[currect_index_alice]
            currect_index_alice+=1


        current_index_merged+=1



    return mergedlist


def testCase():
    assert merge_list([1,2,3],[4,5,6,7])==[1,2,3,4,5,6,7]
    assert merge_list([],[1,2,3])==[1,2,3]
    assert merge_list([1,3],[2,4,6,7])==[1,2,3,4,6,7]



if __name__=="__main__":
    testCase()
