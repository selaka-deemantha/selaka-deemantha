class math_matrix:
    def __init__(self):
        pass
    def mat_mul(self,matrix_1 ,matrix_2):
        ans =[]
        for i in matrix_1:
            tot =0
            for j ,k in zip(i ,matrix_2):
                tot+=( j *k[0])
            ans.append([tot])

        return ans

    def mat_adjoin_3_by_3(self,matrix):
        l=[]
        l2=[]
        ans=[]
        k = 0
        for i in matrix:
            k+=1
            m = 0
            for j in i:
                m+=1
                l.append([j,k,m] )

        for h,i in enumerate(l):

            lst=[j for j in l if j[1] != i[1] and j[2] != i[2]]
            ad=(lst [ 0][0]*lst[ 3 ][0])-(lst [ 1][0]*lst[ 2 ][0])
            if (h+1) % 2 ==0:
                ad=-ad
            l2.append(ad)
            if len(l2)==3:
                ans.append(l2)
                l2=[]
        row1=[]
        row2=[]
        row3=[]
        transpose=[]
        for i in ans:
            row1.append(i[0])
            row2.append(i[1])
            row3.append(i[2])
        transpose.append(row1)
        transpose.append(row2)
        transpose.append(row3)

        return transpose

    def modulus_of_2_by_3_matrix(self,matrix):
        l = []
        l2 = []
        ans = []
        k = 0
        for i in matrix:
            k += 1
            m = 0
            for j in i:
                m += 1
                l.append([j, k, m])

        for h, i in enumerate(l[:4]):

            lst = [j for j in l if j[1] != i[1] and j[2] != i[2]]
            ad = i[0]*((lst[0][0] * lst[3][0]) - (lst[1][0] * lst[2][0]))
            if (h + 1) % 2 == 0:
                ad = -ad
            l2.append(ad)
            if len(l2) == 3:
                return (sum(l2))


    def inverse_of_matrix(self,matrix):
        inv=[]
        modulus=self.modulus_of_2_by_3_matrix(matrix)
        adj_matrix=self.mat_adjoin_3_by_3(matrix)
        for i in adj_matrix:
            inv_r=[]
            for j in i:
                j=j/modulus
                inv_r.append(j)
            inv.append(inv_r)

        return inv





