class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = image[sr][sc]
        if color == m:
            return image
        image[sr][sc] = color
        
        if sc < len(image[0]) - 1and m == image[sr][sc + 1]:
            image = self.floodFill(image, sr, sc + 1, color)
            
        if sr < len(image) - 1 and m == image[sr + 1][sc]:
            image = self.floodFill(image, sr + 1, sc, color)
        
        if sc > 0 and m == image[sr][sc - 1]:
            image = self.floodFill(image, sr, sc - 1, color)
        
        if sr > 0 and m == image[sr - 1][sc]:
            image = self.floodFill(image, sr - 1, sc, color)
        
        return image



"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]

"""