class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #use numbers to set start, end and mid
        #find # of elements on left side and on right
        #if number of elements == k: return 
        #elif num of elements > k: 
        start = matrix[0][0]
        n = len(matrix)-1
        end = matrix[n][n]
    
        while start < end:
            mid = (start + end)//2
            #find left half
            c = self.count(matrix, mid)
            if c < k:
                start = mid +1
            else:
                end = mid
        return start

    
    def count(self, matrix, mid):
        row = len(matrix) -1
        col = 0
        c=0
        while row >=0 and col <=len(matrix)-1:
            if matrix[row][col] <= mid:
                c += row + 1
                col +=1
            else:
                row -=1
        return c