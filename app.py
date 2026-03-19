# ====================
# Import
# ====================
from project import create_app

# ====================
# Create App Instance
# ====================
app = create_app()

# ====================
# Run Server
# ====================
if __name__ == '__main__':
    app.run()
