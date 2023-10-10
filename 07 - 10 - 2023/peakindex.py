class Solution:
     def peakIndexInMountainArray(self, l):
        start=0
        last=len(l)
        mid=(start+last)//2
        def check(start,mid,last):
            if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
                return mid
            elif l[mid-1]>l[mid]:
                return check(mid-2,mid-1,mid)
            elif l[mid+1]>l[mid]:
                return check(mid,mid+1,mid+2)
        return check(start,mid,last)
        return mid