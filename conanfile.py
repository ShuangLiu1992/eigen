from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
import os


class EIGENConan(ConanFile):
    name = "eigen"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps"

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['BUILD_TESTING'] = "OFF"
        tc.variables['EIGEN_BUILD_BLAS'] = "OFF"
        tc.variables['EIGEN_BUILD_LAPACK'] = "OFF"
        tc.variables['EIGEN_BUILD_DOC'] = "OFF"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "none")
        self.cpp_info.builddirs.append(os.path.join("share", "eigen3", "cmake"))
        self.cpp_info.set_property("cmake_file_name", "Eigen3")
