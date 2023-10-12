class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0;
        j = 0;
        if (m!=0) and (n!=0):
            while nums1[i]!=0:
                if nums1[i] > nums2[j]:
                    for k in range(m+j, i, -1):
                        nums1[k] = nums1[k-1];
                    nums1[i] = nums2[j];
                    i = i + 1;
                    j = j + 1;
                else:
                    i = i + 1;
            if j < n:
                for k in range(i, m+n, 1):
                    nums1[k] = nums2[j];
                    j = j + 1;
        if (m==0) and (n!=0):
            for k in range(0, n, 1):
                nums1[k] = nums2[k];
