#!/bin/bash
set -e  # توقف در صورت خطا

echo "📦 نصب پکیج‌ها..."
pip install --no-index --find-links=wheelhouse -r requirements.txt
echo "✅ پکیج‌ها با موفقیت نصب شدند."

