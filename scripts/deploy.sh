#!/bin/bash
set -e

echo "🚀 STARTING DEPLOYMENT PROCESS FOR AWS LAMBDA..."

# GET POETRY'S VIRTUAL ENVIRONMENT PATH
VENV_PATH=$(poetry env info -p)
echo "🔍 Found Poetry virtual environment at: $VENV_PATH"

PYTHON_VERSION="3.12"
SITE_PACKAGES="$VENV_PATH/lib/python$PYTHON_VERSION/site-packages"
BUILD_DIR="build"
PACKAGE_DIR="$BUILD_DIR/lambda_package"
DEPLOYMENT_ZIP="lambda_deployment.zip"

# CLEAN AND CREATE BUILD DIRECTORIES
echo "📁 Creating build directories..."
rm -rf "$BUILD_DIR"
mkdir -p "$PACKAGE_DIR"

# COPY DEPENDENCIES FROM POETRY'S VIRTUALENV
echo "📦 Copying dependencies from Poetry's virtualenv..."
for ITEM in "$SITE_PACKAGES"/*; do
    BASENAME=$(basename "$ITEM")
    
    # SKIP __PYCACHE__ DIRECTORIES AND .PYC FILES
    if [[ "$BASENAME" == "__pycache__" || "$BASENAME" == *.pyc ]]; then
        continue
    fi
    
    # SKIP DISTRIBUTION INFO DIRECTORIES
    if [[ "$BASENAME" == *.dist-info || "$BASENAME" == *.egg-info ]]; then
        continue
    fi
    
    if [ -d "$ITEM" ]; then
        cp -r "$ITEM" "$PACKAGE_DIR"
        # REMOVE __PYCACHE__ DIRECTORIES
        find "$PACKAGE_DIR/$BASENAME" -type d -name "__pycache__" -exec rm -rf {} +
    else
        cp "$ITEM" "$PACKAGE_DIR"
    fi
done

# COPY APPLICATION CODE
echo "📝 Copying application code..."
cp index.py "$PACKAGE_DIR/"

# CREATE DEPLOYMENT PACKAGE
echo "🗜️ Creating deployment package..."
cd "$PACKAGE_DIR"
zip -r "../../$DEPLOYMENT_ZIP" . -x "**/__pycache__/*" "**/*.pyc"
cd "../.."

# REPORT FINAL PACKAGE SIZE
PACKAGE_SIZE=$(du -h "$DEPLOYMENT_ZIP" | cut -f1)
echo "✅ Deployment package created: $DEPLOYMENT_ZIP (Size: $PACKAGE_SIZE)"
echo ""
echo "Next steps:"
echo "1. Upload $DEPLOYMENT_ZIP to AWS Lambda via the AWS console or CLI"
echo "2. Set the Lambda handler to 'index.handler'"
echo "3. Configure API Gateway to integrate with your Lambda function"
