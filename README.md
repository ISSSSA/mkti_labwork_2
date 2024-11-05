# Задание 1
Чтобы помочь Еве расшифровать новое сообщение, воспользуемся уязвимостью повторного использования инициализирующего вектора (IV) и ключа. Если два сообщения зашифрованы в режиме AES-128 OFB с одним и тем же ключом и IV, то они используют один и тот же поток ключей, который можно извлечь с помощью известного открытого текста из предыдущего сообщения.

Подход  
1. Извлечение потока ключей: Так как Ева знает расшифрованный текст первого сообщения и соответствующий шифротекст, она может вычислить поток ключей, который использовался для шифрования этого сообщения, выполнив XOR между шифротекстом и известным открытым текстом.


2. Расшифровка нового сообщения: После получения потока ключей, Ева может применить его к новому шифротексту, чтобы восстановить открытый текст.

Описание уязвимости и устранение
Использование одного и того же IV и ключа для разных сообщений делает шифрование в режиме OFB уязвимым для атак на основе повторного использования IV. Чтобы избежать подобных ситуаций, Бобу следует:

Каждый раз использовать новый уникальный инициализирующий вектор (IV) для каждого сообщения, даже если используется один и тот же ключ.
Сменить ключ для новых сообщений, что ещё больше усложнит расшифровку даже в случае утечки IV.
Эти меры помогут предотвратить повторное использование потока ключей и обеспечат безопасную передачу сообщений.

# Задание 2
Для создания процедуры MixColumns Алисы с новым многочленом $c(x)=α⋅x3+x2+x+(α3+α+1)$  представим его в виде матрицы. При этом нужно учитывать, что операции выполняются в поле $F_{2^8}​$ с элементами, представленными полиномами по модулю неприводимого многочлена $x^8 + x^4 + x^3 + x +1$.

#### 1.1 Построение матрицы MixColumns

Запишем многочлен c(x) как коэффициенты для матрицы преобразования MixColumns. Используя стандартный подход для AES, получаем, что в матричной форме c(x) соответствует следующей матрице:

$M = \begin{pmatrix} \alpha^3 + \alpha + 1 & \alpha & 1 & 1 \\ 1 & \alpha^3 + \alpha + 1 & \alpha & 1 \\ 1 & 1 & \alpha^3 + \alpha + 1 & \alpha \\ \alpha & 1 & 1 & \alpha^3 + \alpha + 1 \end{pmatrix}​​$

#### 1.2 Применение преобразования к вектору (0x15,0xab,0x03,0xf0)

Теперь можно умножить матрицу M на столбец-вектор $(0x15, 0xab, 0x03, 0xf0)^T$, чтобы получить результат преобразования. Умножение выполняется в поле $F_{2^8}$​, что требует использования операций сложения и умножения по модулю неприводимого многочлена $x^8 + x^4 + x^3 + x + 1$. В этом случае каждая операция умножения требует вычисления произведения с последующим приведением по модулю неприводимого многочлена.

#### 1.3 Построение матрицы для обратного преобразования InvMixColumns

Чтобы создать обратное преобразование InvMixColumns, нужно найти обратный многочлен d(x)) к c(x) в кольце $R = F_{2^8}[x] / (x^4 + 1)$. Обратный многочлен d(x) должен удовлетворять условию:

$c(x) \cdot d(x) \equiv 1 \pmod{x^4 + 1}$

Это обратное преобразование будет обеспечивать, что InvMixColumns корректно инвертирует результаты операции MixColumns, возвращая исходные значения.

Боб выбрал многочлен $c(x) = x^2 + 1$ для своей процедуры MixColumns. Однако такой выбор не обеспечивает полноценного линейного смешивания всех четырех байтов столбца. Поскольку этот многочлен имеет степень 2, каждый элемент столбца будет комбинироваться только с соседним элементом, а это недостаточно для построения полной линейной зависимости между всеми элементами вектора. В результате теряется криптографическая стойкость, и корректное восстановление данных при обратном преобразовании становится невозможным.

Таким образом, для корректной работы MixColumns многочлен должен быть степени 3, чтобы каждый элемент вектора зависел от всех остальных элементов, что в данном случае не выполняется.

# Задание 3
Формула: $x_j≡x_0^{2^j}$ для быстрого нахождения $x_j$  
Генерируемая гамма: [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1]  
Расшифрованное сообщение: 11010100010101111110011110001100