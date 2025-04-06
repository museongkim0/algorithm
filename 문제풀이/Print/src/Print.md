# Java Scanner 사용 방법

## 1. Scanner 클래스 임포트
- `java.util.Scanner`를 임포트해야 사용 가능.
```java
import java.util.Scanner;
```

## 2. Scanner 객체 생성
- Scanner 객체를 생성할 때 입력 소스를 지정해야 합니다. 가장 흔히 사용되는 소스는 System.in으로, 키보드 입력을 받습니다.
Scanner sc = new Scanner(System.in);
```java
Scanner sc = new Scanner(System.in);
```

## 3. 입력 받기
- Scanner는 다양한 데이터 타입을 읽을 수 있는 메서드를 제공합니다. 예를 들어:
  - nextLine(): 한 줄의 문자열을 읽음
  - nextInt(): 정수를 읽음
  - nextDouble(): 실수를 읽음
  - next(): 공백 전까지의 문자열을 읽음

## 4. Scanner 사용 후 닫기
- Scanner 객체는 사용이 끝난 후 close() 메서드로 닫아주는 것이 좋습니다. 특히 System.in을 사용할 경우 자원 누수를 방지할 수 있습니다.
```java
sc.close();
```

## 5. Scanner 입력 메서드 표
| 메서드 이름          | 반환 타입   | 설명                                      | 예제 입력       | 예제 코드                     | 예제 출력             |
|----------------------|-------------|-------------------------------------------|-----------------|-------------------------------|-----------------------|
| `next()`            | `String`    | 공백 전까지의 문자열을 읽음               | `Hello World`   | `String word = sc.next();`    | `Hello`              |
| `nextLine()`        | `String`    | 한 줄 전체(개행문자 전까지)를 읽음        | `Hello World`   | `String line = sc.nextLine();`| `Hello World`        |
| `nextInt()`         | `int`       | 정수를 읽음                              | `42`            | `int num = sc.nextInt();`     | `42`                 |
| `nextDouble()`      | `double`    | 실수를 읽음                              | `3.14`          | `double d = sc.nextDouble();` | `3.14`               |
| `nextFloat()`       | `float`     | 단정밀도 실수를 읽음                     | `2.5`           | `float f = sc.nextFloat();`   | `2.5`                |
| `nextLong()`        | `long`      | 긴 정수를 읽음                           | `1234567890`    | `long l = sc.nextLong();`     | `1234567890`         |
| `nextShort()`       | `short`     | 짧은 정수를 읽음                         | `123`           | `short s = sc.nextShort();`   | `123`                |
| `nextByte()`        | `byte`      | 바이트 크기의 정수를 읽음                | `10`            | `byte b = sc.nextByte();`     | `10`                 |
| `nextBoolean()`     | `boolean`   | `true` 또는 `false`를 읽음               | `true`          | `boolean bool = sc.nextBoolean();` | `true`          |
| `nextBigInteger()`  | `BigInteger`| 매우 큰 정수를 읽음 (java.math 필요)     | `1234567890123` | `BigInteger bi = sc.nextBigInteger();` | `1234567890123` |
| `nextBigDecimal()`  | `BigDecimal`| 매우 큰 실수를 읽음 (java.math 필요)     | `12345.6789`    | `BigDecimal bd = sc.nextBigDecimal();` | `12345.6789`    |

## 주의사항
- **공백 처리**: `next()`는 공백 전까지, `nextLine()`은 개행 전까지 읽음.
- **입력 버퍼**: 숫자 입력 후 `nextLine()` 호출 시 버퍼 비우기 필요 (예: `sc.nextLine()` 추가).
- **예외**: 입력 타입 불일치 시 `InputMismatchException` 발생.


# Charactor
## 1. charAt()
1) 문자열에서 문자하나만 가져오는 함수
```java
a = "aBcDeFg";
b = a.charAt(i);
```
## 2. Character.isUpperCase()
1) 문자 값이 대문자 인지 확인
2) 반대로 Character.isLowerCase() 도 있음
```java
if(Character.isUpperCase(b)){}
```
## 3. Character.toUpperCase()
1) 문자 값을 대문자 변환
```java
answer += Character.toUpperCase(b);
```
## 4. Character.toLowerCase()
1) 문자 값을 소문자 변환
```java
answer += Character.toLowerCase(b);
```