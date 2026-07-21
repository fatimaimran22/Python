def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        i=0
        j=0
        nums3=[]
        while i<len(nums1) and j<len(nums2):
                if(nums1[i]<nums2[j]):
                    nums3.append(nums1[i])
                    i+=1
                else:
                    nums3.append(nums2[j])
                    j+=1

        while i<len(nums1):
            nums3.append(nums1[i])
            i+=1

        while j<len(nums2):
            nums3.append(nums2[j])
            j+=1

        length=len(nums3)

        if length%2!=0:
            return nums3[length//2]
        else:
             return (nums3[length//2] + nums3[length//2-1]) /2.0
               

print(findMedianSortedArrays([1,2],[3,4]))