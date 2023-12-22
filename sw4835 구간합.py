T = int(input())
for i in range(T):
    number = list(map(int, input().split()))
    N = number[0]
    M = number[1]
    list1 = list(map(int, input().split()))
    aa = []
    for j in range(N - M + 1):
        aa.append(sum(list1[j:j + M]))
    min1 = min(aa)
    max1 = max(aa)
    print(f'#{i + 1} {max1 - min1}')

# 브루트포스
# 일일이 하나씩 더하기
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     # 최초값 설정
#     max_sum =0
#     min_sum = 987654321
#
#     for i in range(N-M+1):
#         # 슬라이싱 통해 구간합 구하기
#         # N-M은 결국 슬라이싱하는 구간
#         cnt = sum(nums[i:i+M])
#
#         # 최대값 및 최소값 갱신
#         max_sum = max(cnt, max_sum)
#         min_sum = min(cnt, min_sum)
#
#     print(f'#{tc} {max_sum - min_sum}')
#   시간 복잡도 = M*(N-M-1) == O(M*N)   거의 O(n^2)


# 슬라이딩 윈도우
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#
#     # 첫 번째 범위의 값 구하기
#     cnt = sum(nums[:M])
#     # 최초값 설정
#     max_sum = cnt
#     min_sum = cnt
#
#     for i in range(N-M):
#         # 슬라이딩 윈도우: 가장 왼쪽 값 빼고 다음 오른쪽 값 더하기
#         cnt += nums[i + M] - nums[i]
#
#         # 최대값 및 최소값 갱신
#         max_sum = max(cnt, max_sum)
#         min_sum = min(cnt, min_sum)
#
#     print(f'#{tc} {max_sum - min_sum}')
# 시간 복잡도 = M+2*(N-M-2) == O(N)
#

# 누적합  -> 미리 계산해 놓은다
# N+2*(N=M+1) == O(N)
