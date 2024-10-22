def findKthLargest(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)-k]
    
def findKthLargest_heapsort(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def rebulid_heap(heap,left,right):
            high = left
            temp = heap[high]
            i = left * 2
            while i < right:
                
                if i+1 < right and heap[i] < heap[i+1]:
                    i += 1
                if heap[i] > heap[high]:
                    # heap[i],heap[high] = heap[high],heap[i]
                    # high = i
                    heap[high] = heap[i]
                    high = i
                else:
                    break
                
                i = i * 2        
            heap[high] = temp
        n = len(nums)
        m = int(n/2)
        
        for i in range(m-1,-1,-1):
            rebulid_heap(nums,i,n)
        
        for i in range(k):
            nums[0],nums[n-1-i] = nums[n-1-i],nums[0]
            rebulid_heap(nums,i,n-i-1)
                
        return nums[-k]
        
def findKthLargest_quicksort(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def cut(nums,left,right,k):
            n = len(nums)
            i = left 
            j = right - 1
            base = nums[i]
            while i < j:
                while nums[j] >= base and j >i:
                    j -= 1
                nums[i] = nums[j]
                while nums[i] <= base and i < j:
                    i += 1
                nums[j] = nums[i]
            nums[i] = base
            return i

        def Quick_sort(nums,left,right,k):
            
            if right - left <= 1:
                return -1
            middle = cut(nums,left,right,k)
            if middle == n-k:
                return middle
            
            a = Quick_sort(nums,left,middle,k)
            
            b = Quick_sort(nums,middle+1,right,k)
            
            return max(a,b)
                
        n = len(nums)
        return Quick_sort(nums,0,n,k)
        # return nums
       
if __name__ == '__main__':
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    ans1 = findKthLargest_quicksort(nums1,k1)
    print(ans1)