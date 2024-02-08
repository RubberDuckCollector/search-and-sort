-- chatGPT gave me this code
insertionSort :: (Ord a) => [a] -> [a]
insertionSort [] = []
insertionSort (x : xs) = insert x (insertionSort xs)
  where
    insert :: (Ord a) => a -> [a] -> [a]
    insert x [] = [x]
    insert x (y : ys)
      | x <= y = x : y : ys
      | otherwise = y : insert x ys

main :: IO ()
main = do
  let inputArray = [9, 5, 3, 7, 2, 8, 4, 1, 6, 0]
  putStrLn "Input Array:"
  print inputArray
  putStrLn "Sorted Array (using Insertion Sort):"
  let sortedArray = insertionSort inputArray
  print sortedArray
