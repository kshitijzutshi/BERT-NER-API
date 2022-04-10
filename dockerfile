FROM public.ecr.aws/lambda/python:3.8

# Copy function code and models into our /var/task
COPY ./ ${LAMBDA_TASK_ROOT}/

# install our dependencies
RUN python3 -m pip install https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp38-cp38-linux_x86_64.whl transformers==3.4.0 --target ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "handler.handler"]
