# Exercise of slam/liegroup

请完善src/LieGroup.h，实现类函数并通过测试,提交LieGroup.h到作业文件夹．


## 接口说明

需要实现：
1. 已知相机位置，相机ｚ朝向，－ｙ轴朝向，求相机到世界坐标系变换
2. 坐标系间转换练习
3. 旋转矩阵的log,exp
4. SE3的log,exp
5. R*p及T*p李代数求导

```
#ifndef SUMMERCAMP_LIEGROUP_H
#define SUMMERCAMP_LIEGROUP_H

#include <Eigen/Dense>
#include <GSLAM/core/GSLAM.h>

namespace summercamp {

class LieGroup{
public:
    typedef Eigen::Vector3d Vector3d;
    typedef Eigen::Matrix<6,1,double> Vector6d;
    typedef Eigen::Matrix3d Matrix3d;
    typedef Eigen::Matrix<3,4,double> Matrix34d;
    typedef Eigen::Matrix<4,4,double> Matrix4d;
    typedef Eigen::Matrix<3,6,double> Matrix36d;

    // Please return the camera to world transformation T_wc
    // P_w=T_wc*P_c
    static Matrix4d lookAt(Vector3d translation, // this means the position of the camera
                            Vector3d lookAtPoint, // this means the z axis direction
                            Vector3d up);         // this means the -y axis direction

    // Coordinates: IMU, Camera, World
    // T_cw : world to left camera
    // T_ic : left camera to imu
    // Please return the IMU to world transformation T_wi
    static Matrix4d transfomMulti(Matrix4d Tcw,Matrix4d Tic);

    // Given a rotation matrix R, please return the lie algebra log(R)
    static Vector3d log(Matrix3d R);

    // Given the rotation lie algebra so3, please return the rotation matrix R
    static Matrix3d exp(Vector3d so3);

    // Given a transform matrix T, please return the lie algebra log(T)
    static Vector6d log(Eigen::Matrix4d T);

    // Given the transform lie algebra se3, please return the transform matrix T
    static Matrix4d exp(Vector6d se3);

    // Given rotation lie algebra \xi , 3d point p,
    // please return \frac{\partial{exp(\xi)*p}}{\partial{p}}
    static Matrix3d jacobianP(Vector3d xi,Vector3d p);

    // Given rotation R, 3d point p, sub to: R=exp(\xi)
    // please return \frac{\partial{R*p}}{\partial{\xi}}
    static Matrix3d jacobianR(Matrix3d R,Vector3d p);

    // Given SE3 T, 3d point p, sub to : T=exp(\xi)
    // please return \frac{\partial{T*p}}{\partial{\xi}}
    static Matrix36d jacobianT(Matrix4d T,Vector3d p);
};

}
#endif

```
