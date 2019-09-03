## What is the difference between concurrency and parallelism?

reference: https://medium.com/mr-efacani-teatime/concurrency%E8%88%87parallelism%E7%9A%84%E4%B8%8D%E5%90%8C%E4%B9%8B%E8%99%95-1b212a020e30

- ## Concurrency: 
multi-thread, there are threads handling different part of works to make one thing done, they share same memory region along with variables.

Example: Multo-thread process, take a process apart, runing those partitions simultaneously.

- ## Parallelism: 
multi-process, there are process doing one identical thing, using different region of memory region.

Example: Load balance, deploy several identical services or webpages, lead visitors to them to decrease loading in one.

#
- Pros of multi-process\
-Speed: multi-process > multi-thread\
-Safety: If some part died, multi-thread must die, but multi-process might suvive.

- Cons of multi-process\
-Computing resource: multi-process > multi-thread\
-Memory usage: multi-process > multi-thread

#
## Python multi-thread
Python 不支援真正意義上的多執行緒程式設計。在 Python 中有一個叫做 GIL 的東西，中文是 全域性直譯鎖 ，這東西控制了 Python，讓 Python 只能同時執行一個執行緒。相當於說真正意義上的多執行緒是由 CPU 來控制的，Python 中的多執行緒由 GIL 控制。如果有一個 CPU 密集型程式，用 C 語言寫的，執行在一個四核處理器上，採用多執行緒技術的話最多可以獲得 4 倍的效率提升，但是如果用 Python 寫的話並不會有提高，甚至會變慢，因為執行緒切換的問題。所以 Python 多執行緒相對更加適合寫 I/O 密集型程式，再說了真正的對效率要求很高的 CPU 密集型程式都用 C/C 去了。

## GIL 
GIL是一個貨真價實的全域性執行緒鎖,在直譯器解釋執行任何 Python 程式碼時,都需要先獲得這把鎖才行,在遇到 I/O 操作時會釋放這把鎖。只有獲得了全域性直譯器鎖的執行緒才能操作 Python 物件或者呼叫 Python/C API 函式。為了支援多執行緒 Python 程式設計,直譯器有規律的釋放和回收鎖——預設情況下,每100位元組指令集迴圈一次(可以通過sys.setcheckinterval()設定)。

## 在多執行緒環境中,Python 虛擬機器的執行方式
1.設定GIL\
2.切換到一個執行緒去執行\
3.執行: \
a. 指定數量的位元組碼指令,或者 \
b. 執行緒主動讓出控制(可以呼叫time.sleep(0))\
4.把執行緒設定為睡眠狀態\
5.解鎖GIL\
6.再次重複以上所有步驟

## Conclusion
In python, only use multi-thread with I/O bound operation. CPU operation let C handle if we need more efficiency.
