FROM python:3.9
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"
WORKDIR /home/user/app
COPY --chown=user . .
# Agar requirements file hai toh ye line chalao, warna rehne do
RUN pip install --no-cache-dir openai numpy pandas || true
EXPOSE 7860
CMD ["python", "-u", "inference.py"]
