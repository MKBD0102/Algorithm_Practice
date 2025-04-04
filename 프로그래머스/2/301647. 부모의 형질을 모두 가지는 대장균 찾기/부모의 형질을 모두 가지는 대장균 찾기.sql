SELECT C.ID AS ID, C.GENOTYPE AS GENOTYPE,  P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA C LEFT JOIN ECOLI_DATA P ON C.PARENT_ID = P.ID
WHERE C.GENOTYPE & P.GENOTYPE = P.GENOTYPE
ORDER BY C.ID