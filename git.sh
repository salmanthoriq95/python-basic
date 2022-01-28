message=$1
branch=$2
echo "[START] FETCH AND PULL FROM GITHUB AND GITLAB (1/5)"
git fetch --all
git pull gitlab $branch
git pull github $branch
echo "[END] FETCH AND PULL FROM GITHUB AND GITLAB (1/5)"
echo ""

echo "[START] GIT STATUS (2/5)"
git status
echo "[END] GIT STATUS (2/5)"
echo ""

echo "[START] ADD AND COMMIT ALL FILES (3/5)"
git add *
git commit -a -m "$message"
echo "[END] ADD AND COMMIT ALL FILES (3/5)"
echo ""

echo "[START] PUSH COMMITS TO GITLAB AND GITHUB (4/5)"
git push gitlab $branch
git push github $branch
echo "[END] PUSH COMMITS TO GITLAB AND GITHUB (4/5)"
echo ""

echo "[START] GIT STATUS (5/5)"
git status
echo "[END] GIT STATUS (5/5)"
echo ""