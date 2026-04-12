FROM python:3.9

# User set up for Hugging Face
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"
WORKDIR /home/user/app

COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY --chown=user . .

# Port 7860 Hugging Face ke liye zaroori hai
EXPOSE 7860

CMD ["python", "-u", "inference.py"]
