# ===========================
# 🐍 Miniconda & Conda Cheat Sheet
# ===========================

# 🔧 1. Start Conda (activate base environment)
# Open terminal and run:
# $ conda activate

# 🆕 2. Create a new Python environment
# Syntax: conda create --name <env_name> python=<version>
# Example:
# $ conda create --name myenv python=3.11

# ✅ 3. Activate the environment
# $ conda activate myenv

# ❌ 4. Deactivate the current environment
# $ conda deactivate

# 📜 5. List all Conda environments
# $ conda env list

# 📦 6. Install a package into the active environment
# Syntax: conda install <package_name>
# Example:
# $ conda install numpy pandas matplotlib

# 🌐 7. Install from conda-forge channel (community maintained)
# Example:
# $ conda install -c conda-forge jupyterlab

# 📝 8. Export current environment to a file (for sharing)
# $ conda env export > environment.yml

# 📥 9. Create env from an environment.yml file
# $ conda env create -f environment.yml

# 🔁 10. Update environment based on a YAML file
# $ conda env update --file environment.yml --prune

# 🗑 11. Remove an environment
# $ conda env remove --name myenv

# 🔎 12. List packages in the active environment
# $ conda list

# 🆚 13. Check Conda version
# $ conda --version

# 🛠 14. Update Conda itself
# $ conda update -n base -c defaults conda

# 🧼 15. Clean up unused packages and cache
# $ conda clean --all

# 🚀 BONUS: Launch Jupyter Notebook in the active env
# $ conda install jupyter
# $ jupyter notebook

# 🧠 TIP: Use `mamba` for faster installs (drop-in replacement for conda)
# $ conda install mamba -n base -c conda-forge
# Then use:
# $ mamba install <package_name>