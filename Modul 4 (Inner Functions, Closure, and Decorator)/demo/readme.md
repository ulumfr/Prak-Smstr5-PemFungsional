## Perhitungan Transformasi sesuai NIM 

### NIM yang digunakan adalah 3 digit terakhir [xyz]
- [x,y,z] -> [4,6,2]
- A[x,y] -> A[4,6]
- B[y,z] -> B[6,2]

#### Transformasi:
- M = x -> M = 4
- tx = y -> tx = 6
- ty = z -> ty = 2
- sx = z -> sx = 2
- sy = x -> sy = 4

#### Mengalami Transformasi Beruntun: 
- Nim Genap -> (awal) Titik A (3, 4) dan Titik B (5,6)
- Nim Genap -> (nim) Titik A (4, 6) dan Titik B (6,2)

##### Diketahui: 
- (awal) Koordinat translasi (tx, ty) = (2, 3)
- (nim) Koordinat translasi (tx, ty) = (6, 2)

- sudut rotasi = 60 derajat

- (awal) Koordinat dilatasi (sx, sy) = (1.5, 2)
- (nim) Koordinat dilatasi (sx, sy) = (2, 4)

##### Ditanya:
1. Tentukan Persamaan Garis Hasil Transformasi!

##### Jawaban:
1. Translasi terhadap (tx, ty) = (6, 2)
    - Titik A(4, 6) -> A'(4+6, 6+2) = A'(10, 8)
    - Titik B(6, 2) -> B'(6+6, 2+2) = B'(12, 4)

2. Rotasi sejajar sumbu x positif sebesar 60 derajat

    - Titik A'(10, 8)
        - x' = xcos(60°) - ysin(60°)
        - y' = xsin(60°) + ycos(60°)

        - x' = 10cos(60°) - 8sin(60°)
        - y' = 10sin(60°) + 8cos(60°)

        - x' = 10 * (1/2) - 8 * (v3/2)
        - y' = 10 * (v3/2) + 8 * (1/2)

        - x' = 5 - 4v3
        - y' = 5v3 + 4

        Jadi (-1.9282032302755079, 12.660254037844386)<br><br>
    
    - Titik B'(12, 4)
        - x' = xcos(60°) - ysin(60°)
        - y' = xsin(60°) + ycos(60°)

        - x' = 12cos(60°) - 4sin(60°)
        - y' = 12sin(60°) + 4cos(60°)

        - x' = 12 * (1/2) - 4 * (v3/2)
        - y' = 12 * (v3/2) + 4 * (1/2)

        - x' = 6 - 2v3
        - y' = 6v3 + 2

        Jadi, (2.5358983848622474, 12.392304845413264)<br><br>

3. Perbesaran Skala Rotasi 
    - Titik A" (-1.9282032302755079, 12.660254037844386) dengan (2, 4)
        - x' = sx * x
        - y' = sy * y
        - x' = 2 * -1.9282032302755079
        - y' = 4 * 12.660254037844386
        - x' = -3.8564064605510158
        - y' = 50.64101615137754
        
        Jadi, (-3.8564064605510158, 50.64101615137754)<br><br>

    - Titik B" (2.5358983848622474, 12.392304845413264) dengan (2, 4)
        - x' = sx * x
        - y' = sy * y
        - x' = 2 * 2.5358983848622474
        - y' = 4 * 12.392304845413264
        - x' = 5.071796769724495
        - y' = 49.569219381653056
        
        Jadi, (5.071796769724495, 49.569219381653056)<br><br>



4. Persamaan garis yang melalui titik A (-3.8564064605510158, 50.64101615137754) dan titik B (5.071796769724495, 49.569219381653056)
    - y = mx - c
    - m = (y2 - y1) / (x2 - x1)
    - m = (-0.120046)
    - 50.64101615137754 = (-0.120046)(-3.8564064605510158) - C
    - c = 51.104107499933974
    - y = (-0.12)x + 51.104

